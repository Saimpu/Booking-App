import React from "react";

const RoomInfo = ({ room }) => {
  return (
    <div className="room-info">
      <h2>{room.name}</h2>
      <p>
        <strong>Type:</strong> {room.types}
      </p>
      <p>
        <strong>Price per Night:</strong> {room.currency} {room.pricepernight}
      </p>
      <p>
        <strong>Max Occupancy:</strong> {room.maxOccupency} guests
      </p>
      <p className="description">{room.description}</p>
    </div>
  );
};

export default RoomInfo;