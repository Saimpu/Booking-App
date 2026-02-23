import React, { useContext } from "react";
import RoomImageSlider from "./RoomImageSlider";
import RoomInfo from "./Roominfo";
import "./RoomDetails.css";
import { UserContext } from "./UserContext";
import { useNavigate } from "react-router-dom";

const RoomCard = ({ room, selectedDateRange, onBookingSuccess }) => {
  const { user } = useContext(UserContext);
  const navigate = useNavigate();

  const handleBooking = async (roomId, userId, selectedDateRange) => {
    if (!user) return navigate("/auth");

    const baseURL = "https://booking-app-a6cv.onrender.com/api";

    const startDate = new Date(selectedDateRange.startDate);
    const endDate = new Date(
      selectedDateRange.endDate || selectedDateRange.startDate
    );

    for (
      let currentDate = new Date(startDate);
      currentDate <= endDate;
      currentDate.setDate(currentDate.getDate() + 1)
    ) {
      try {
        const response = await fetch(`${baseURL}/occupied/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${user.token}`,
          },
          body: JSON.stringify({
            room: `${baseURL}/roomBooking/${roomId}/`,
            user: `${baseURL}/users/${userId}/`,   // change if endpoint name different
            date: currentDate.toISOString().split("T")[0],
          }),
        });

        const data = await response.json();
        console.log("SERVER RESPONSE:", data);

        if (!response.ok) throw new Error(JSON.stringify(data));
      } catch (error) {
        console.error("Error during booking:", error);
        return;
      }
    }

    onBookingSuccess();
  };

  // Convert backend images → slider format
  const imageList = room.images?.map((img) => img.image) || [];

  return (
    <div className="room-card">
      <RoomImageSlider images={imageList} />
      <RoomInfo room={room} />

      <button
        className="book-room-button"
        onClick={() => handleBooking(room.id, user?.user?.id, selectedDateRange)}
        disabled={!selectedDateRange?.startDate}
      >
        Book Room
      </button>
    </div>
  );
};

export default RoomCard;
