import "../css/cards.css";

function StatCard({

    title,

    value,

    icon,

    color

}){

    return(

        <div className="statCard">

            <div
                className="statIcon"
                style={{background:color}}
            >

                {icon}

            </div>

            <div>

                <p className="statTitle">

                    {title}

                </p>

                <h2 className="statValue">

                    {value}

                </h2>

            </div>

        </div>

    )

}

export default StatCard;