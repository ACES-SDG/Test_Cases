import React, { useState } from "react";
import { FaTrash } from 'react-icons/fa';
import Papa from "papaparse";
import Plot from 'react-plotly.js';
import Granularity from "./Granularity";
import aggregateFunctions from "aggregate-functions";


const allowedExtensions = ["csv"];
const Sheet =()=>{
  

    const [csvfile,setFile] = useState('');
    const [error, setError] = useState("");
    const [data,setData] = useState([]);
    const [csvArray, setCsvArray] = useState([]);
    const [rowValue,setRowValue] = useState([]);
    const [columnValue,setColumnValue] = useState([]);
    const [selectedRowValue , setSelectedRowValue] = useState('Select Row Value');
    const [selectedColumnValue , setSelectedColumnValue] = useState('Select Column Value');
    const[typeGraph, setTypeGraph] = useState('');

    
       //Drag and Drop
   let dragged
   const handleDrag = (e)=>{
    dragged = e.target
  }
 const handleDrop = (e)=>{
    
    e.preventDefault()

    const dragValue = dragged.innerText;
    setSelectedRowValue(dragValue);
    const rowPlotValue = csvArray.map(record => record[dragValue]);
    // console.log(rowPlotValue)
    setRowValue(rowPlotValue);
   }

    const dragOver=(e)=>{
        e.preventDefault();
    }
    const changeDrop = (e)=>{
     
        const dragValue = dragged.innerText;
        setSelectedColumnValue(dragValue);
        const columnPlotValue = csvArray.map(record => record[dragValue]);
        console.log(columnPlotValue);
        setColumnValue(columnPlotValue);
    }
    
    const processCsv = (str,delim = ',')=>{ // to get particular row/column data
        const headers = str.slice(0,str.indexOf('\n')).split(delim) ;
        const rows = str.slice(0,str.indexOf('\n+1')).split('\n') ;
        const newArray = rows.map(row=>{
          const values= row.split(delim);
          const eachObject = headers.reduce((obj , header, i)=>{
            obj[header] = values[i];
            return obj;
          },{})
          return eachObject;
        })
       setCsvArray(newArray)
      //  console.log(typeof newArray)
      }
    //TO Display columns in Datafield
    const handleFileChange = (e) => {
        setError("");
        if (e.target.files.length) {
        const inputFile = e.target.files[0];
      
    const fileExtension = inputFile?.type.split("/")[1];
    if (!allowedExtensions.includes(fileExtension)) {
            setError("Please input a csv file");
            return;
        }

        setFile(inputFile);
    }};
    const handleColumns=()=>{
        const file = csvfile;
        const reader = new FileReader();
        reader.onload = async ({ target }) => {
            const text = target.result;
           const csv = Papa.parse(target.result, { header: true });
           const parsedData = csv?.data;
           const columns = Object.keys(parsedData[0]);
           setData(columns);
           processCsv(text);
          //  console.log(target.file.name);
         
       };

       reader.readAsText(file);
   };
   
   ///Graph Selection

   const selectGraph=(e)=>{
        if(e.target.className == "selectGraph"){
            // const x = e.target.value;
            const selectGraphs = e.target.value;
            setTypeGraph(selectGraphs)

        }
}
//Delete Values
  const deleteRowValues = (e)=>{
    rowValue.filter(index => index !== e);
    setSelectedRowValue()
  
  }
  const deleteColumnValues = (e)=>{
    columnValue.filter(index => index !== e);
    setSelectedColumnValue()
  }
  
  var a = csvArray;
  var b = columnValue;
  var union = [...new Set([...a, ...b])];
  console.log(union);

    return(
        <>
         <div>
        </div>
         <div className="First-line">
            
         <select>
            <option>Files</option>
            <option>New</option>
            <option>Open</option>
            <option>Save</option>
            <option>Exit</option>


         </select>
         <select>
            <option>Data</option>
            <option>@</option> 
         </select>
         <select>
            <option>WorkSheet</option>
            <option>@</option>
         </select>
         <select>
            <option>Dashboard</option>
            <option>@</option>
         </select>

     </div>
     <hr></hr>
     <div className="Second-line" >
         <h3>Home</h3>
         <h3>Left</h3>
         <h3>Right</h3>

     </div>
<hr></hr>
     <div className="third-line">
         
     <div className="field">
         
     <input
                onChange={handleFileChange}
                id="csvInput"
                name="file"
                type="File"
                accept=""
            />
     <select onClick={handleColumns}>
     <option>Datafield</option>
     </select>
     <div className="display" >
        {error ? error : data.map((columns, id) =>
        <div draggable onDragStart={handleDrag} key={id}>{columns}</div>
        )}
     </div>
            
         </div>
         <hr className="vl"></hr>

         <div className="filter">

         <select><option>Filters</option></select>
         <select><option>Marks</option></select>
         <select><option>Pages</option></select>
      
          {/* <Granularity/> */}
         </div>
       
        
        <div className="graph" >
            <p droppable  className="dropzone" 
            onDragOver={dragOver} onDrop={handleDrop}
            >
            Row:{selectedRowValue}
            <FaTrash onClick={deleteRowValues}style={{cursor:"pointer"}}/></p>
         <br></br>
         <hr style={{width:"700px"}}></hr>

         <p droppable  className="dropzone" 
            onDragOver={dragOver} onDrop={changeDrop}>Column:{selectedColumnValue}
         <FaTrash onClick={deleteColumnValues}style={{cursor:"pointer"}} />
         </p>
        <br></br>
         <select className="selectGraph"  onChange={selectGraph} style={{background:"green"}}>Graph
             <option value='Graph'>Graph</option>
             <option value="Line">Line-Graph</option>
             <option value="Bar">Bar Chart</option>
             <option value="Pie">Pie-Chart</option>
      
         </select>
         {/* <select className="Aggregate" style={{background:"grey"}}>
             <option value='Sum'>Sum</option>
             <option value="Min">Min</option>
             <option value="Max">Max</option>
             <option value="Count">Count</option>
             <option value="Avg">Avg</option>

      
         </select> */}
         
{typeGraph ==="Bar"?
    <div className="">
    <Plot  

data={[
  
  {type: 'bar',
  mode: '',
  x:columnValue,
   y: rowValue,
  
  transforms:[{
    type:'aggregate',

    aggregations:[{
      target:'y',
      func:'Sum',
      enabled:true
    }]
  }]
  },
]}

layout={ {
  // autosize: false,
  xaxis:columnValue,
  yaxis:rowValue,
  
   updatemenus:[{
     x:0.85,
     y:1.05,
     
showactive: true,
    buttons: [
     
      {
        method: 'restyle',
        args: ['transforms[0].aggregations[0].func', 'sum'],
        label: 'Sum'
    },{
      
      method: 'restyle',
      args: ['transforms[0].aggregations[0].func', 'avg'],
      label: 'Avg'
  }, {
    method: 'restyle',
      args: ['transforms[0].aggregations[0].func', 'min'],
      label: 'Min'
  }, {
    method: 'restyle',
      args: ['transforms[0].aggregations[0].func', 'max'],
      label: 'Max'
  }, {
      method: 'restyle',
      args: ['transforms[0].aggregations[0].func', 'mode'],
      label: 'Mode'
  }, {
      method: 'restyle',  
      args: ['transforms[0].aggregations[0].func', 'median'],
      label: 'Median'
  }, 
  {
    method: 'restyle',  
    args: ['transforms[0].aggregations[0].func', 'count'],
    label: 'Count'
  }, {
    
      method: 'restyle',   
      args: ['transforms[0].aggregations[0].func', 'stddev'],
      label: 'Std.Dev'
  }, {
    

    method: 'restyle',   
      args: ['transforms[0].aggregations[0].func', 'first'],
      label: 'First'
  }, {
    method: 'restyle',   
      args: ['transforms[0].aggregations[0].func', 'last'],
      label: 'Last'
  }]
     
   }]
   } }

  

/>
</div>
:  typeGraph==="Line" ? 
<div className="">
<Plot  

data={[

{type: 'line',
mode: 'lines+markers',
x:columnValue,
y: rowValue,

transforms:[{
type:'aggregate',

aggregations:[{
  target:'y',
  func:'Sum',
  enabled:true
}]
}]
},
]}

layout={ {
// autosize: false,
xaxis:columnValue,
yaxis:rowValue,

updatemenus:[{
 x:0.85,
 y:1.05,
 
showactive: true,
buttons: [
 
  {
    method: 'restyle',
    args: ['transforms[0].aggregations[0].func', 'sum'],
    label: 'Sum'
},{
  
  method: 'restyle',
  args: ['transforms[0].aggregations[0].func', 'avg'],
  label: 'Avg'
}, {
method: 'restyle',
  args: ['transforms[0].aggregations[0].func', 'min'],
  label: 'Min'
}, {
method: 'restyle',
  args: ['transforms[0].aggregations[0].func', 'max'],
  label: 'Max'
}, {
  method: 'restyle',
  args: ['transforms[0].aggregations[0].func', 'mode'],
  label: 'Mode'
}, {
  method: 'restyle',  
  args: ['transforms[0].aggregations[0].func', 'median'],
  label: 'Median'
}, 
{
method: 'restyle',  
args: ['transforms[0].aggregations[0].func', 'count'],
label: 'Count'
}, {

  method: 'restyle',   
  args: ['transforms[0].aggregations[0].func', 'stddev'],
  label: 'Std.Dev'
}, {


method: 'restyle',   
  args: ['transforms[0].aggregations[0].func', 'first'],
  label: 'First'
}, {
method: 'restyle',   
  args: ['transforms[0].aggregations[0].func', 'last'],
  label: 'Last'
}]
 
}]
} }



/>
</div>: typeGraph==="Pie" ?<div className="">
    <Plot  

data={[
  
  {type: 'pie',
  mode: 'lines+markers',
  values:rowValue,
  

  },
]}


  

/>
</div>:<div>{null}</div>}



   
</div>
       </div>
      
        </>
    )
}

export default Sheet;