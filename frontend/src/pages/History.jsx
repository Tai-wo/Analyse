import MainLayout from "../layouts/MainLayout";
import "../css/History.css";

function History() {

    const history = [

        {
            action: "Uploaded Sales.xlsx",
            time: "2 mins ago",
            status: "Completed"
        },

        {
            action: "Generated Python Analysis",
            time: "12 mins ago",
            status: "Completed"
        },

        {
            action: "Created Pivot Table",
            time: "25 mins ago",
            status: "Completed"
        },

        {
            action: "Generated SQL Queries",
            time: "1 hour ago",
            status: "Completed"
        },

        {
            action: "Exported Tableau Dashboard",
            time: "Yesterday",
            status: "Completed"
        }

    ];

    return (

        <MainLayout>

            <div className="history-page">

                <div className="history-header">

                    <h1>Activity History</h1>

                    <p>

                        View every analysis, upload and export you've made.

                    </p>

                </div>

                <div className="history-card">

                    {

                        history.map((item,index)=>(

                            <div
                                className="history-item"
                                key={index}
                            >

                                <div>

                                    <h3>{item.action}</h3>

                                    <small>{item.time}</small>

                                </div>

                                <span className="status">

                                    {item.status}

                                </span>

                            </div>

                        ))

                    }

                </div>

            </div>

        </MainLayout>

    );

}

export default History;