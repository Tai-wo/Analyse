import MainLayout from "../layouts/MainLayout";
import "../css/Settings.css";

import {

User,

Moon,

Bell,

Shield,

Save

} from "lucide-react";

function Settings(){

    return(

        <MainLayout>

            <div className="settings-page">

                <div className="pageHeader">

                    <h1>Settings</h1>

                    <p>

                        Customize your Analyse experience.

                    </p>

                </div>

                <div className="settingsGrid">

                    <div className="settingCard">

                        <User size={40}/>

                        <h3>Profile</h3>

                        <p>Manage your account.</p>

                    </div>

                    <div className="settingCard">

                        <Moon size={40}/>

                        <h3>Appearance</h3>

                        <p>Dark & Light mode.</p>

                    </div>

                    <div className="settingCard">

                        <Bell size={40}/>

                        <h3>Notifications</h3>

                        <p>Email and alerts.</p>

                    </div>

                    <div className="settingCard">

                        <Shield size={40}/>

                        <h3>Security</h3>

                        <p>Password & authentication.</p>

                    </div>

                </div>

                <button className="saveButton">

                    <Save size={18}/>

                    Save Changes

                </button>

            </div>

        </MainLayout>

    )

}

export default Settings;