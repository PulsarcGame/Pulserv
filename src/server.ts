import { Database } from "./data/database";
import { Player } from "./data/tables/player";
import { Map } from "./data/tables/map";

class Server {
    private static db : Database;

    constructor() {
    }
    
    public init() {
        Server.db = new Database();

        console.log("Created DB");

        Server.db.getUser(1).then( (user:Player) => {
            console.log(user.id);
        });

        Server.db.getMap(1).then( (map:Map) => {
            console.log(map.title);
        });
    }
}


var server = new Server();

server.init();