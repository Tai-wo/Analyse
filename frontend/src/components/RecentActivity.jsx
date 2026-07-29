import "../css/recentActivity.css";

function RecentActivity(){

    const activity=[

        "Uploaded Sales.xlsx",

        "Generated Python Code",

        "Created Pivot Table",

        "Generated SQL",

        "Exported Dashboard"

    ];

    return(

        <div className="activityCard">

            <h2>Recent Activity</h2>

            {

                activity.map((item,index)=>(

                    <div

                        className="activityItem"

                        key={index}

                    >

                        {item}

                    </div>

                ))

            }

        </div>

    );

}

export default RecentActivity;