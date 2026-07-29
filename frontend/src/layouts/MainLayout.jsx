import Sidebar from "../components/Sidebar";

function MainLayout({ children }) {

    return (

        <div
            style={{
                display: "flex",
                minHeight: "100vh",
                background: "#f5f7fb"
            }}
        >

            <Sidebar />

            <div
                style={{
                    flex: 1,
                    marginLeft: "260px",
                    overflowY: "auto"
                }}
            >

                {children}

            </div>

        </div>

    );

}

export default MainLayout;