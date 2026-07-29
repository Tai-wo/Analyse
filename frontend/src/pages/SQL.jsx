import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import "../css/tools.css";

function SQL(){

const tools=[

"SELECT",

"WHERE",

"GROUP BY",

"HAVING",

"ORDER BY",

"JOIN",

"UNION",

"WINDOW FUNCTIONS",

"CTE",

"Stored Procedures"

];

return(

<>

<Sidebar/>

<Navbar/>

<div className="tools">

<h1>SQL Generator</h1>

{

tools.map(tool=>(

<label key={tool}>

<input type="checkbox"/>

{tool}

</label>

))

}

<button>

Generate SQL

</button>

</div>

</>

)

}

export default SQL;
