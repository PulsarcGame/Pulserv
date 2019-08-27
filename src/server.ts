import { Database } from "./data/database";

class Server {
    private static db : Database;

    constructor() {
    }
    
    public async init() {
        Server.db = new Database();
        //Server.db.modelize();

        console.log("Created DB");

        const user = await Server.db.getUser(1);
        const map = await Server.db.getMap(1);

        console.log(user);
    }
}


var server = new Server();

server.init();