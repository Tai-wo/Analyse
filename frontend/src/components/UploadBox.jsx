import {

UploadCloud

} from "lucide-react";

import "../css/cards.css";

function UploadBox({

    onChange

}){

    return(

        <label className="uploadBox">

            <UploadCloud

                size={70}

            />

            <h2>

                Drag & Drop Dataset

            </h2>

            <p>

                CSV • Excel • XLSX

            </p>

            <input

                type="file"

                hidden

                onChange={onChange}

            />

        </label>

    )

}

export default UploadBox;