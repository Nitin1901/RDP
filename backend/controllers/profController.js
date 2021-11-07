import Professor from "../models/Professor.js";
import asyncHandler from "express-async-handler";
import mongoose from "mongoose";

//@desc     Get all professors
//@route    GET /api/professors
//@access   public
export const getProfessors = asyncHandler(async (req, res) => {
  const data = await Professor.find();

  res.send(data);
});
