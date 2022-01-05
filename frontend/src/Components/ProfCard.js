import * as React from 'react';
import { Card, Button, CardMedia, Avatar } from '@mui/material/';
import CardContent from '@mui/material/CardContent';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { useSelector } from 'react-redux';
import { CardActions, Grid } from '@mui/material';

const ProfCard = ({ data, history }) => {
  const learnMoreHandler = () => {
    history.push(`/profile/${data._id}`);
  };

  return (
    <Grid item xs={11} md={6} p={1}>
      <Card sx={{ minWidth: 275 }}>
        <CardContent>
          <Avatar
            src={data.profile_picture}
            alt="green iguana"
            sx={{ height: 100, width: 100, margin: 2 }}
          />

          <Typography variant="h5" component="div">
            {data.name}
          </Typography>
          <Typography color="text.secondary">{data.affiliations.designation}</Typography>
          <Typography color="text.secondary">{data.affiliations.department}</Typography>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            {data.affiliations.university}
          </Typography>
        </CardContent>
        <CardActions sx={{ alignItems: 'center', justifyContent: 'center' }}>
          <Button size="small" onClick={learnMoreHandler}>
            Learn More
          </Button>
        </CardActions>
      </Card>
    </Grid>
  );
};
export default ProfCard;
