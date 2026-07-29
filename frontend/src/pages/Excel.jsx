import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import "../css/tools.css";

function Excel(){

const tools=[

"Data Cleaning",

"Remove Duplicates",

"Missing Values",

"Pivot Tables",

"Charts",

"Formula Generator",

"Conditional Formatting",

"Sorting",

"Filtering",

"Dashboard"

];

return(

<>

<Sidebar/>

<Navbar/>

<div className="tools">

<h1>Excel Analytics</h1>

{

tools.map(tool=>(

<label key={tool}>

<input type="checkbox"/>

{tool}

</label>

))

}

<button>

Run Analysis

</button>

</div>

</>

)

}

export default Excel;
