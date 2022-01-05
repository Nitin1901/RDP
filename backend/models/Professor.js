import mongoose from 'mongoose';

const researcherSchema = new mongoose.Schema({
  name: String,
  research_interests: [],
  research_area: String,
  affiliations: {
    designation: String,
    university: String,
    department: String,
  },
});

const Researcher = mongoose.model('Researcher', researcherSchema, 'Researchers');
export default Researcher;
