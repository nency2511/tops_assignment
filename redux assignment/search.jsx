// Create a Table and Search data from table using React Js?

import React, { useState } from "react";

const App = () => {
  // Sample data
  const [data, setData] = useState([
    { id: 1, name: "John", age: 28 },
    { id: 2, name: "Jane", age: 24 },
    { id: 3, name: "Mike", age: 30 },
    { id: 4, name: "Emma", age: 22 },
  ]);

  // State to handle search query
  const [searchQuery, setSearchQuery] = useState("");

  // Function to filter data based on search query
  const filteredData = data.filter((item) =>
    item.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div>
      <h1>Searchable Table</h1>
      {/* Search input */}
      <input
        type="text"
        placeholder="Search by name..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />

      {/* Table */}
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {filteredData.length > 0 ? (
            filteredData.map((item) => (
              <tr key={item.id}>
                <td>{item.id}</td>
                <td>{item.name}</td>
                <td>{item.age}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="3">No results found</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default App;
