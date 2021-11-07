import express from "express";
import { getProfessors } from "../controllers/profController.js";

const router = express.Router();

//Get all professor route
router.route("/").get(getProfessors);

export default router;
