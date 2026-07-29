import {Database} from "lucide-react";

import "../css/cards.css";

function DatasetCard({

    name,

    rows,

    columns,

    onOpen

}){

    return(

        <div className="datasetCard">

            <Database
                size={45}
            />

            <h3>

                {name}

            </h3>

            <div className="datasetInfo">

                <span>

                    {rows} Rows

                </span>

                <span>

                    {columns} Columns

                </span>

            </div>

            <button

                onClick={onOpen}

            >

                Open Workspace

            </button>

        </div>

    )

}

export default DatasetCard;