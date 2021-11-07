import * as React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Link from "@mui/material/Link";
import Typography from "@mui/material/Typography";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { useSelector } from "react-redux";
import { Grid } from "@mui/material";

const ProfCard = ({ data }) => {
  const setProfessorSpecialisation = useSelector(
    (state) => state.setProfessorSpecialisation
  );
  const { specialisation } = setProfessorSpecialisation;
  let match = "true";
  if (data.interests === null) {
    match = undefined;
  }
  if (specialisation !== "" && data.interests !== null) {
    match = data.interests.find((element) => {
      if (element.includes(specialisation)) {
        return true;
      }
    });
  }
  if (specialisation !== "" && match !== undefined) {
    return (
      <Grid item xs={11} md={6} p={1}>
        <Card sx={{ minWidth: 275 }}>
          <CardContent>
            <Typography
              sx={{ fontSize: 14 }}
              color="text.secondary"
              gutterBottom
            >
              <Link href={data.profile} target="_blank" rel="noreferrer">
                Profile
              </Link>{" "}
              |{" "}
              <Link href={data.website} target="_blank" rel="noreferrer">
                Website
              </Link>{" "}
              |{" "}
              <Link
                href={`maito:${data.contact.email}`}
                target="_blank"
                rel="noreferrer"
              >
                Email
              </Link>
            </Typography>
            <Typography variant="h5" component="div">
              {data.name}
            </Typography>
            <Typography color="text.secondary">
              {data.affiliations[0].designation} |{" "}
              {data.affiliations[0].department}
            </Typography>
            <Typography sx={{ mb: 1.5 }} color="text.secondary">
              {data.affiliations[0].university}
            </Typography>
            <Typography variant="body2">
              <strong>Education: </strong> {data.education}
            </Typography>
            <Typography variant="body2">
              <strong>Phone: </strong> {data.contact.ph_num}
            </Typography>
            <Typography variant="body2">
              <Accordion sx={{ mx: 3 }}>
                <AccordionSummary
                  expandIcon={<ExpandMoreIcon />}
                  aria-controls="panel1a-content"
                  id="panel1a-header"
                >
                  <Typography>Interests</Typography>
                </AccordionSummary>
                <AccordionDetails>
                  {data.interests &&
                    data.interests.map((interest, i) => {
                      return (
                        <Typography>
                          {i + 1}. {interest}{" "}
                        </Typography>
                      );
                    })}
                </AccordionDetails>
              </Accordion>{" "}
            </Typography>
          </CardContent>
        </Card>
      </Grid>
    );
  } else if (specialisation !== "" && match === undefined) {
    return null;
  } else if (specialisation === "") {
    return (
      <Grid item xs={11} md={6} p={1}>
        <Card sx={{ minWidth: 275 }}>
          <CardContent>
            <Typography
              sx={{ fontSize: 14 }}
              color="text.secondary"
              gutterBottom
            >
              <Link href={data.profile} target="_blank" rel="noreferrer">
                Profile
              </Link>{" "}
              |{" "}
              <Link href={data.website} target="_blank" rel="noreferrer">
                Website
              </Link>{" "}
              |{" "}
              <Link
                href={`maito:${data.contact.email}`}
                target="_blank"
                rel="noreferrer"
              >
                Email
              </Link>
            </Typography>
            <Typography variant="h5" component="div">
              {data.name}
            </Typography>
            <Typography color="text.secondary">
              {data.affiliations[0].designation} |{" "}
              {data.affiliations[0].department}
            </Typography>
            <Typography sx={{ mb: 1.5 }} color="text.secondary">
              {data.affiliations[0].university}
            </Typography>
            <Typography variant="body2">
              <strong>Education: </strong> {data.education}
            </Typography>
            <Typography variant="body2">
              <strong>Phone: </strong> {data.contact.ph_num}
            </Typography>
            <Typography variant="body2">
              <Accordion sx={{ mx: 3 }}>
                <AccordionSummary
                  expandIcon={<ExpandMoreIcon />}
                  aria-controls="panel1a-content"
                  id="panel1a-header"
                >
                  <Typography>Interests</Typography>
                </AccordionSummary>
                <AccordionDetails>
                  {data.interests &&
                    data.interests.map((interest, i) => {
                      return (
                        <Typography>
                          {i + 1}. {interest}{" "}
                        </Typography>
                      );
                    })}
                </AccordionDetails>
              </Accordion>{" "}
            </Typography>
          </CardContent>
        </Card>
      </Grid>
    );
  }
};
export default ProfCard;
