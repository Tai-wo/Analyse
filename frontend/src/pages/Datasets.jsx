import MainLayout from "../layouts/MainLayout";
import "../css/Datasets.css";

import {

Database,

Eye,

Trash2,

FolderOpen

} from "lucide-react";

function Datasets(){

    const datasets=[

        {
            id:1,
            name:"Sales.xlsx",
            rows:5240,
            columns:18
        },

        {
            id:2,
            name:"Customers.csv",
            rows:3200,
            columns:12
        },

        {
            id:3,
            name:"Finance.xlsx",
            rows:2100,
            columns:15
        }

    ];

    return(

        <MainLayout>

            <div className="datasets-page">

                <div className="pageHeader">

                    <h1>Datasets</h1>

                    <p>
                        Manage all uploaded datasets.
                    </p>

                </div>

                <div className="datasetTable">

                    <table>

                        <thead>

                            <tr>

                                <th>ID</th>

                                <th>Name</th>

                                <th>Rows</th>

                                <th>Columns</th>

                                <th>Actions</th>

                            </tr>

                        </thead>

                        <tbody>

                        {

                            datasets.map((item)=>(

                                <tr key={item.id}>

                                    <td>{item.id}</td>

                                    <td>

                                        <Database size={18}/>

                                        {item.name}

                                    </td>

                                    <td>{item.rows}</td>

                                    <td>{item.columns}</td>

                                    <td>

                                        <button>

                                            <Eye size={18}/>

                                        </button>

                                        <button>

                                            <FolderOpen size={18}/>

                                        </button>

                                        <button>

                                            <Trash2 size={18}/>

                                        </button>

                                    </td>

                                </tr>

                            ))

                        }

                        </tbody>

                    </table>

                </div>

            </div>

        </MainLayout>

    )

}

export default Datasets;