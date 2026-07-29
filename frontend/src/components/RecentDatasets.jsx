import "../css/recentDatasets.css";

function RecentDatasets() {

    const datasets = [

        {
            name: "Sales.xlsx",
            rows: 5200,
            columns: 18
        },

        {
            name: "Customers.csv",
            rows: 3200,
            columns: 9
        },

        {
            name: "Finance.xlsx",
            rows: 2100,
            columns: 12
        }

    ];

    return (

        <div className="recentCard">

            <h2>Recent Datasets</h2>

            <table>

                <thead>

                    <tr>

                        <th>Name</th>

                        <th>Rows</th>

                        <th>Columns</th>

                    </tr>

                </thead>

                <tbody>

                    {

                        datasets.map((data, index)=>(

                            <tr key={index}>

                                <td>{data.name}</td>

                                <td>{data.rows}</td>

                                <td>{data.columns}</td>

                            </tr>

                        ))

                    }

                </tbody>

            </table>

        </div>

    );

}

export default RecentDatasets;