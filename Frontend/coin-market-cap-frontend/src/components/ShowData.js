import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'

function ShowData(props) {
    const [data, setData] = useState([]);

    useEffect(() => {
        let interval = setInterval(async () => {
            const request_options = {
                method: "GET",
                headers: {
                    "X-CSRFToken": window.CSRF_TOKEN,
                    "content-type": "application/json"
                }
            };
            let data = await fetch(props.url, request_options);
            data = await data.json();
            setData(data);
        }, 3000);

        return () => {
            clearInterval(interval);
        }
    }, [])

  return (
    <div>
        <table className='table table-hover'>
            <thead>
                <tr>
                    <th>name</th>
                    <th>price</th>
                    <th>perc_1h</th>
                    <th>perc_24h</th>
                    <th>perc_7d</th>
                    <th>market_cap</th>
                    <th>volume_24h</th>
                    <th>circulating_supply</th>
                </tr>
            </thead>
            <tbody>
                {
                    data.map((record, index)=>{
                        return (
                            <tr key={index}>
                                <td>{record["name"]}</td>
                                <td>{record["price"]}</td>
                                <td>{record["perc_1h"]}</td>
                                <td>{record["perc_24h"]}</td>
                                <td>{record["perc_7d"]}</td>
                                <td>{record["market_cap"]}</td>
                                <td>{record["volume_24h"]}</td>
                                <td>{record["circulating_supply"]}</td>
                            </tr>
                        )
                    })
                }
            </tbody>
        </table>

        
    </div>
  )
}

ShowData.propTypes = {}

export default ShowData
