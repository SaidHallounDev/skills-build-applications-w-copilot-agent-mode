import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Teams endpoint:', endpoint);
        console.log('Fetched teams:', results);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [endpoint]);

  return (
    <div className="mb-4">
      <h2 className="mb-4 display-6">Teams</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="table-dark">
            <tr>
              {teams.length > 0 && Object.keys(teams[0]).map((key) => (
                <th key={key}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {teams.map((team, idx) => (
              <tr key={team.id || idx}>
                {teams.length > 0 && Object.keys(teams[0]).map((key) => (
                  <td key={key}>{String(team[key])}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
        {teams.length === 0 && <div className="alert alert-info">No teams found.</div>}
      </div>
    </div>
  );
};

export default Teams;
