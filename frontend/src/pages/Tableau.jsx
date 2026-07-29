import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import "../css/tools.css";

function Tableau(){

const dashboards=[

"Sales Dashboard",

"KPI Dashboard",

"Executive Dashboard",

"Maps",

"Forecast",

"Bar Charts",

"Line Charts",

"Pie Charts",

"Scatter Plot",

"Story"

];

return(

<>

<Sidebar/>

<Navbar/>

<div className="tools">

<h1>Tableau Builder</h1>

{

dashboards.map(item=>(

<label key={item}>

<input type="checkbox"/>

{item}

</label>

))

}

<button>

Generate Dashboard

</button>

</div>

</>

)

}

export default Tableau;
