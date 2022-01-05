import Researcher from '../models/Professor.js';
import asyncHandler from 'express-async-handler';
import mongoose from 'mongoose';

//@desc     Get all professors
//@route    GET /api/professors
//@access   public
export const getProfessors = asyncHandler(async (req, res) => {
  //Pagnination
  const pageSize = 50;
  const page = Number(req.query.pageNumber) || 1;

  //If keyword exists then we pass regex to the find function
  const keyword =
    req.query.keyword != 'undefined'
      ? {
          $or: [
            {
              research_interests: {
                $regex: req.query.keyword,
                $options: 'i',
              },
            },
            {
              name: {
                $regex: req.query.keyword,
                $options: 'i',
              },
            },
            {
              affiliations: {
                $regex: req.query.keyword,
                $options: 'i',
              },
            },
          ],
        }
      : {};

  const count = await Researcher.count({ ...keyword });

  //.limit to get onlt the pagesize number of products
  //.skip to get the required pageSize products
  const data = await Researcher.find({ ...keyword })
    .limit(pageSize)
    .skip(pageSize * (page - 1));

  console.log(keyword);
  res.status(200).json({ data, page, pages: Math.ceil(count / pageSize) });
});

//@desc     Get a professor detail
//@route    GET /api/professors/:id
//@access   public
export const getProfessor = asyncHandler(async (req, res) => {
  const id = req.params.id;
  const data = await Researcher.findById(id);
  console.log(data);
  if (!data) {
    res.status(404);
    throw new Error('Researcher Not Found');
  }
  res.status(200).json(data);
});
