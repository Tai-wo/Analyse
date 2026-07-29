import "../css/cards.css";

function FeatureCard({

    title,

    description,

    icon,

    onClick

}){

    return(

        <div

            className="featureCard"

            onClick={onClick}

        >

            <div className="featureIcon">

                {icon}

            </div>

            <h2>

                {title}

            </h2>

            <p>

                {description}

            </p>

            <button>

                Open →

            </button>

        </div>

    )

}

export default FeatureCard;