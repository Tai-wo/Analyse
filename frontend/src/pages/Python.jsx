import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import "../css/tools.css";

function Python(){

const tools=[

"Profiling",

"Pandas Summary",

"Correlation",

"Regression",

"Classification",

"Clustering",

"Forecasting",

"Machine Learning",

"Visualization",

"Auto ML"

];

return(

<>

<Sidebar/>

<Navbar/>

<div className="tools">

<h1>Python Analytics</h1>

{

tools.map(tool=>(

<label key={tool}>

<input type="checkbox"/>

{tool}

</label>

))

}

<button>

Run Analysis</button>

</div>

</>

)

}

export default Python;
