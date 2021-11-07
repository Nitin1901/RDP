import mongoose from "mongoose";

const professorSchema = new mongoose.Schema({});

const Professor = mongoose.model("Professor", professorSchema, "Professor");
export default Professor;
