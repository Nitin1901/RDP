import express from "express";
import { getProfessor, getProfessors } from "../controllers/profController.js";

const router = express.Router();

//Get all professor route
router.route("/").get(getProfessors);
router.route("/:id").get(getProfessor);

export default router;
