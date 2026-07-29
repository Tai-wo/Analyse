import MainLayout from "../layouts/MainLayout";
import "../css/upload.css";

import {
    UploadCloud,
    FileSpreadsheet,
    FileText,
    Sparkles
} from "lucide-react";

function Upload() {

    return (

        <MainLayout>

            <div className="upload-page">

                <div className="pageHeader">

                    <h1>Upload Dataset</h1>

                    <p>

                        Upload Excel or CSV files and let Analyse AI
                        automatically understand your data.

                    </p>

                </div>

                <div className="uploadContainer">

                    <div className="uploadCard">

                        <UploadCloud
                            size={75}
                            className="uploadIcon"
                        />

                        <h2>

                            Drag & Drop Files

                        </h2>

                        <p>

                            Upload .xlsx or .csv files

                        </p>

                        <input
                            type="file"
                            accept=".xlsx,.csv"
                        />

                        <button>

                            Upload Dataset

                        </button>

                    </div>

                    <div className="uploadInfo">

                        <div className="infoBox">

                            <FileSpreadsheet size={45}/>

                            <h3>

                                Excel Files

                            </h3>

                            <p>

                                Clean, analyze, generate charts,
                                pivot tables and AI reports.

                            </p>

                        </div>

                        <div className="infoBox">

                            <FileText size={45}/>

                            <h3>

                                CSV Files

                            </h3>

                            <p>

                                Automatic profiling and cleaning.

                            </p>

                        </div>

                        <div className="infoBox">

                            <Sparkles size={45}/>

                            <h3>

                                AI Ready

                            </h3>

                            <p>

                                Generate Python, SQL,
                                Tableau and Excel outputs.

                            </p>

                        </div>

                    </div>

                </div>

            </div>

        </MainLayout>

    );

}

export default Upload;