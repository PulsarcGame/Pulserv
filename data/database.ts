import { Sequelize } from "sequelize";
import { ExecException } from "child_process";
import { Player } from './tables/player';
import { Map } from "./tables/map";

export class Database {
    private static sequelize: Sequelize;
    private static config : any;

    public constructor() {
        try {
            Database.config = require("../pulserv.json");
        } catch {
            throw "ERROR: Missing config. Please fill the required fields in pulserv.json file, using pulserv.json.example.";
        }
        Database.sequelize = new Sequelize(
            Database.config.database.dbname,
            Database.config.database.login,
            Database.config.database.pass,
            {
                host: Database.config.database.host,
                port: Database.config.database.port,
                dialect: Database.config.database.dialect
            }
        );

        Database.sequelize
            .authenticate()
            .then((): void => {
                console.log('Connection has been established successfully.');
            })
            .catch((err: ExecException): void => {
                console.error('Unable to connect to the database:', err);
            });
    }

    public async getUser(id : number) : Promise<Player> {
        var user = (await Database.sequelize.query("SELECT * FROM player WHERE id = "+id))[0][0];
        return new Player(user.id, user.username, user.mail);
    }

    public async getMap(id : number) : Promise<Map> {
        var map = (await Database.sequelize.query("SELECT * FROM map WHERE id = "+id))[0][0];
        return new Map(map.id, map.set_id, map.title, map.artist, map.version, map.mapper, map.difficulty);
    }
}