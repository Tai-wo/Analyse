import MainLayout from "../layouts/MainLayout";
import FeatureCard from "../components/FeatureCard";

import {
    FaFileExcel,
    FaPython,
    FaDatabase,
    FaChartBar
} from "react-icons/fa";

import { useNavigate } from "react-router-dom";

import "../css/features.css";

function Features() {

    const navigate = useNavigate();

    return (

        <MainLayout>

            <div className="features-page">

                <h1>Choose Analytics Engine</h1>

                <div className="feature-grid">

                    <FeatureCard
                        icon={<FaFileExcel size={70}/>}
                        title="Excel"
                        description="Cleaning • Pivot Tables • Charts"
                        onClick={() => navigate("/excel")}
                    />

                    <FeatureCard
                        icon={<FaPython size={70}/>}
                        title="Python"
                        description="Pandas • Machine Learning • AI"
                        onClick={() => navigate("/python")}
                    />

                    <FeatureCard
                        icon={<FaDatabase size={70}/>}
                        title="SQL"
                        description="AI Query Builder"
                        onClick={() => navigate("/sql")}
                    />

                    <FeatureCard
                        icon={<FaChartBar size={70}/>}
                        title="Tableau"
                        description="Interactive Dashboards"
                        onClick={() => navigate("/tableau")}
                    />

                </div>

            </div>

        </MainLayout>

    );

}

export default Features;