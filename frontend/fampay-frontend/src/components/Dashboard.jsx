// src/components/Dashboard.js
import React, { useState, useEffect } from "react";
import axios from "axios";
import './dashboard.css'
const backend_url = "http://localhost:8000"

const Dashboard = () => {
  const [videos, setVideos] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(false);

  // Fetch all videos on initial load
  useEffect(() => {
    fetchVideos();
  }, []);

  // Function to fetch videos from the API
  const fetchVideos = async (query = "") => {
    setLoading(true);

    try {
      const url = query
        ? `${backend_url}/api/searchVideos?query=${query}`
        : `${backend_url}/api/getVideos`; 

      const response = await axios.get(url);
      console.log(response)
      if(!query) setVideos(response.data.results || [])
      else setVideos(response.data.data || [])
    } catch (error) {
      console.error("Error fetching videos:", error);
    }

    setLoading(false);
  };

  // Handle search input change
  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  // Handle search submit
  const handleSearchSubmit = (event) => {
    event.preventDefault();
    fetchVideos(searchQuery);
  };

  return (
    <div className="dashboard">
      <h1>Video Dashboard</h1>

      {/* Search bar */}
      <form onSubmit={handleSearchSubmit}>
        <input
          type="text"
          value={searchQuery}
          onChange={handleSearchChange}
          placeholder="Search videos..."
        />
        <button type="submit">Search</button>
      </form>

      {loading && <p>Loading...</p>}

      <div className="video-list">
        {videos.length === 0 && !loading ? (
          <p>No videos found</p>
        ) : (
          videos.map((video) => (
            <div key={video.video_id} className="video-item">
              <img
                src={video.thumb_url || "default_thumbnail.jpg"} 
                alt={video.video_title}
                className="video-thumbnail"
              />
              <h3>{video.video_title}</h3>
              <p>{video.video_description}</p>
              <p>{new Date(video.pub_date).toLocaleDateString()}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Dashboard;
