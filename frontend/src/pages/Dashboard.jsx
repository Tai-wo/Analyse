import MainLayout from "../layouts/MainLayout";
import Topbar from "../components/Topbar";

import DashboardStats from "../components/DashboardStats";
import QuickActions from "../components/QuickActions";
import RecentDatasets from "../components/RecentDatasets";
import AIInsights from "../components/AIInsights";
import RecentActivity from "../components/RecentActivity";

import "../css/dashboard.css";

function Dashboard(){

    return(

        <MainLayout>

            <Topbar/>

            <div className="page">

                <div className="hero">

                    <div>

                        <span className="heroBadge">

                            AI Powered Analytics Platform

                        </span>

                        <h1>

                            Welcome back, Taiwo 👋

                        </h1>

                        <p>

                            Analyse helps you clean, explore, visualize and generate AI-powered insights from your datasets in seconds.

                        </p>

                    </div>

                    <div className="heroImage">

                        📊🤖

                    </div>

                </div>

                <DashboardStats/>

                <QuickActions/>

                <div className="dashboardGrid">

                    <RecentDatasets/>

                    <AIInsights/>

                </div>

                <RecentActivity/>

            </div>

        </MainLayout>

    )

}

export default Dashboard;