
export default class {

    public id: number;
    public set_id: number;

    public title: string;
    public artist: string;
    public version: string;

    public mapper: number;
    public difficulty: string;

    constructor(id_: number, set_id_: number, title_: string, artist_: string, version_: string, mapper_: number, difficulty_: string) {
        this.id = id_;
        this.set_id = set_id_;
        this.title = title_;
        this.artist = artist_;
        this.version = version_;
        this.mapper = mapper_;
        this.difficulty = difficulty_;
    }
}