import "../css/dashboardStats.css";

import {

Database,

Brain,

FolderOpen,

HardDrive

} from "lucide-react";

function DashboardStats(){

const stats=[

{

title:"Datasets",

value:"14",

icon:<Database size={34}/>

},

{

title:"AI Analyses",

value:"83",

icon:<Brain size={34}/>

},

{

title:"Workspaces",

value:"9",

icon:<FolderOpen size={34}/>

},

{

title:"Storage",

value:"2.4 GB",

icon:<HardDrive size={34}/>

}

];

return(

<div className="statsGrid">

{

stats.map((item,index)=>(

<div

className="statCard"

key={index}

>

<div className="statIcon">

{item.icon}

</div>

<div>

<h2>

{item.value}

</h2>

<p>

{item.title}

</p>

</div>

</div>

))

}

</div>

)

}

export default DashboardStats;