const fs = require('fs');
const chalk = require('chalk');
const notesfunction = ()=>"Notes here";

const addNote = (title,body)=>{
    const notes = loadNotes();

    var check=0;

    for(var i in notes)
    {
        if(notes[i].title===title)
            check=1;          
    }
    
   /* const duplicateNotes =  notes.filter((note)=>note.title===title);*/
    //if(duplicateNotes.length===0){
    if(check==0){
    notes.push({
        title: title,
        body: body
    });

    console.log(notes);
    saveNotes(notes);
}else{
    console.log("Title already exists!!!");
}
};

const removeNote = (title)=>{
        var remcheck=0;
        var index;
        var notes=[];
        var j=0;
        const rem = loadNotes();
        //const notes = rem.filter((r)=>r.title!===title);
        for(var i in rem)
        {
            if(rem[i].title===title)
               {
                    remcheck=1;
                    index=i;
               }
            else{
                
                notes.push({
                    title:rem[i].title,
                    body:rem[i].body
                });
            }
        }
        if(remcheck===0)
        {
            console.log(chalk.bgRed('No such title exists'));
        }else{
            try{
           // delete rem[index];
            saveNotes(notes);
            console.log(chalk.bgGreen("deleted sucessfully"));
            console.log(notes);
             } catch(e){
                console.log(`Error!!${e}`);
            }
        }
}

const saveNotes = (notes)=>{
    const dataJSON = JSON.stringify(notes);
    fs.writeFileSync('notes.json',dataJSON);
}
const readNote = (title)=>{
    const notes = loadNotes();
    var check=0,index;
    for(var i in notes)
    {
        if(notes[i].title===title)
        {
            check=1;
            index=i;
        }
    }
    if(check===0){
        console.log("No notes found");
    }else{
        try{
                console.log("Title:",notes[index].title,"\nBody:",notes[index].body);
        }catch(e){
            console.log("Error found!!"+e);
        }
    }
}
const listNotes = ()=>{
    const notes = loadNotes();
    console.log('Your Notes are:\n');
    for(var i in notes){
        console.log(`Title ${(parseInt(i)+1)}:${notes[i].title}\nBody:${notes[i].body}\n`);
    }
}
const loadNotes = ()=>{
    try{
        const dataBuffer = fs.readFileSync('notes.json');
        const dataJSON = dataBuffer.toString();
        return JSON.parse(dataJSON);
    }
    catch(e){
        return []
    }
};
module.exports={
    notesfunction: notesfunction,
    addNote: addNote,
    removeNote:removeNote,
    readNote:readNote,
    listNotes:listNotes
}