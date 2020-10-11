const yargs = require('yargs');
const chalk = require('chalk');
const notes = require('./notes.js');

yargs.command({
    command:'add',
    describe:'Add a new note',
    builder: {
        title:{
            describe:'Note Title',
            demand:true,
            type:'string'
        },
        body:{
            describe:'Note Body',
            demand:true,
            type:'string'
        }
    },
    handler: (argv)=>{
        //console.log('Title:',argv.title,'\nBody:',argv.body);
        notes.addNote(argv.title,argv.body);
    }

});

yargs.command({
    command:'remove',
    describe:'removing a note',
    builder: {
                title:{
                    describe:"Note Title",
                    demand:true,
                    type:'string'
                }
    },
    handler:(argv)=>{
        notes.removeNote(argv.title);
    }
});

yargs.command({
    command:'read',
    describe:'read a note',
    builder:{
                title:{
                    describe:"Read Title",
                    demand:true,
                    type:'string'
                }
    },
    handler:(argv)=>{
       // console.log('Listing...');
       notes.readNote(argv.title);
    }
});
yargs.command({
    command:'list',
    describe:'list all notes',
    handler:()=>{
        notes.listNotes();
        //console.log('Reading a note');
    }
});
yargs.parse();
//console.log(yargs.argv);