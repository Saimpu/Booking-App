import React, { useState } from "react";

const RoomImageSlider = ({ images = [] }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  // Safety: no images
  if (!images || images.length === 0) {
    return <div className="image-slider">No Image Available</div>;
  }

  const handlePrev = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0 ? images.length - 1 : prevIndex - 1
    );
  };

  const handleNext = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === images.length - 1 ? 0 : prevIndex + 1
    );
  };

  return (
    <div className="image-slider">
      <button onClick={handlePrev}>&#10094;</button>

      <img
        src={images[currentIndex]}   // ⭐ FIXED HERE
        alt="Room"
        className="slider-image"
      />

      <button onClick={handleNext}>&#10095;</button>
    </div>
  );
};

export default RoomImageSlider;