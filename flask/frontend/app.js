const express = require("express");
const bodyParser = require("body-parser");
const fetch = require("node-fetch");

const app = express();

app.set("view engine","ejs");

app.use(bodyParser.urlencoded({extended:true}));

const BACKEND = process.env.BACKEND_URL || "http://backend:5000";

app.get("/",(req,res)=>{

    res.render("index",{error:null});

});

app.post("/submit",async(req,res)=>{

    try{

        const response = await fetch(`${BACKEND}/submit`,{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                itemName:req.body.itemName,
                itemDescription:req.body.itemDescription
            })

        });

        const data = await response.json();

        if(data.success){

            res.redirect("/success");

        }else{

            res.render("index",{error:data.message});

        }

    }

    catch(err){

        res.render("index",{error:err.message});

    }

});

app.get("/success",(req,res)=>{

    res.render("success");

});

app.listen(3000,()=>{

    console.log("Frontend running");

});