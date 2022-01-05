import React, { useState, useEffect } from 'react';
import {
  Grid,
  TextField,
  InputAdornment,
  IconButton,
  Avatar,
  Typography,
  CardContent,
  CardActions,
  Card,
  Button,
  Divider,
} from '@mui/material';
import ProfCard from '../../Components/ProfCard';
import SearchIcon from '@mui/icons-material/Search';
import Loader from '../../Components/Loader';
import { getProfessorDetail } from '../../Actions/profActions';
import { useDispatch, useSelector } from 'react-redux';
import './ProfileScreen.css';

const ProfileScreen = ({ match }) => {
  const id = match.params.id;

  const professorDetail = useSelector((state) => state.professorDetail);
  let { loading, error, professorInfo: data } = professorDetail;

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getProfessorDetail(id));
  }, [id]);

  return (
    <>
      <Grid
        pt={2}
        container
        align="center"
        justifyContent="center"
        sx={{ border: 'solid 1px #dfdfdf', minHeight: '100vh', margin: 2 }}
      >
        {loading ? (
          <Loader />
        ) : (
          <>
            <Grid item xs={12} md={3} p={1}>
              <Avatar
                alt="Remy Sharp"
                src={data.profile_picture}
                className="avatar"
                sx={{ height: 160, width: 160, mx: 1 }}
              />
            </Grid>
            <Grid item xs={12} md={9} p={1}>
              <Card>
                <CardContent sx={{ textAlign: 'left' }}>
                  <Typography sx={{ fontSize: 20 }} variant="h3" gutterBottom>
                    {data.name}
                  </Typography>
                  <Typography variant="h5" component="div"></Typography>
                  <Typography color="text.secondary">
                    {data.affiliations.designation} | {data.affiliations.department}
                  </Typography>
                  <Typography sx={{ mb: 1.5 }} color="text.secondary">
                    {data.affiliations.university}
                  </Typography>

                  <Typography variant="body2">
                    <a href={data.profile_link}>Profile Link</a>
                  </Typography>
                </CardContent>
              </Card>
              {/* Education */}
              {data.education && (
                <Card sx={{ my: 2 }}>
                  <CardContent sx={{ textAlign: 'left' }}>
                    <Typography sx={{ fontSize: 20 }} variant="h3" gutterBottom>
                      Education
                    </Typography>

                    {data.education.map((ed) => {
                      return (
                        <>
                          <Typography sx={{ fontSize: 17 }} variant="h3" gutterBottom>
                            {ed.university} {ed.duration && '(' + ed.duration + ')'}
                          </Typography>
                          <Typography color="text.secondary">{ed.degree}</Typography>
                          <Divider sx={{ my: 2 }} />
                        </>
                      );
                    })}
                  </CardContent>
                </Card>
              )}

              {data.experience && (
                <Card sx={{ my: 2 }}>
                  <CardContent sx={{ textAlign: 'left' }}>
                    <Typography sx={{ fontSize: 20 }} variant="h3" gutterBottom>
                      Experience
                    </Typography>

                    {data.experience.map((ex) => {
                      return (
                        <>
                          <Typography sx={{ fontSize: 17 }} variant="h3" gutterBottom>
                            {ex.designation} {ex.duration && '(' + ex.duration + ')'}
                          </Typography>
                          <Typography color="text.secondary">{ex.department}</Typography>

                          <Typography color="text.secondary">{ex.university}</Typography>
                          <Divider sx={{ my: 2 }} />
                        </>
                      );
                    })}
                  </CardContent>
                </Card>
              )}

              <Card>
                <CardContent sx={{ textAlign: 'left' }}>
                  <Typography sx={{ fontSize: 20 }} variant="h3" gutterBottom>
                    Interests
                  </Typography>

                  <Typography sx={{ fontSize: 16 }} variant="h3" gutterBottom>
                    <strong>Area of Research:</strong> {data.research_area}
                  </Typography>
                  <Typography color="text.secondary">
                    {data.research_interests.map((interest) => interest + ',')}
                  </Typography>
                </CardContent>
              </Card>

              {data.publications && (
                <Card sx={{ my: 2 }}>
                  <CardContent sx={{ textAlign: 'left' }}>
                    <Typography sx={{ fontSize: 20 }} variant="h3" gutterBottom>
                      Publications
                    </Typography>

                    {data.publications.map((pb) => {
                      return (
                        <>
                          <Typography sx={{ fontSize: 17 }} variant="h3" gutterBottom>
                            {pb.title}
                          </Typography>
                          <Typography color="text.secondary">
                            {pb.authors.length > 0 &&
                              pb.authors.map((pba) => {
                                return pba + ' ';
                              })}
                          </Typography>
                          <Typography color="text.secondary">
                            {pb.journal} {pb.volume && `Vol: (${pb.volume})`}{' '}
                            {pb.year && `Year: (${pb.year})`}
                          </Typography>
                          <Divider sx={{ my: 2 }} />
                        </>
                      );
                    })}
                  </CardContent>
                </Card>
              )}

              {data.patents && (
                <Card sx={{ my: 2 }}>
                  <CardContent sx={{ textAlign: 'left' }}>
                    <Typography sx={{ fontSize: 20 }} variant="h3" gutterBottom>
                      Patents
                    </Typography>

                    {data.patents.map((pt) => {
                      return (
                        <>
                          <Typography sx={{ fontSize: 17 }} variant="h3" gutterBottom>
                            {pt.name}
                          </Typography>
                          <Typography color="text.secondary">{pt.authors}</Typography>
                          <Typography color="text.secondary">{pt.patent_number}</Typography>
                          <Divider sx={{ my: 2 }} />
                        </>
                      );
                    })}
                  </CardContent>
                </Card>
              )}

              {data.projects && (
                <Card sx={{ my: 2 }}>
                  <CardContent sx={{ textAlign: 'left' }}>
                    <Typography sx={{ fontSize: 20 }} variant="h3" gutterBottom>
                      Projects
                    </Typography>

                    {data.projects.map((pj) => {
                      return (
                        <>
                          <Typography sx={{ fontSize: 17 }} variant="h3" gutterBottom>
                            {pj.name}
                          </Typography>
                          {pj.details.map((pjd) => {
                            return <Typography color="text.secondary">{pjd} </Typography>;
                          })}
                          <Divider sx={{ my: 2 }} />
                        </>
                      );
                    })}
                  </CardContent>
                </Card>
              )}
              {data.academic_identity && (
                <Card sx={{ my: 2 }}>
                  <CardContent sx={{ textAlign: 'left' }}>
                    <Typography sx={{ fontSize: 20 }} variant="h3" gutterBottom>
                      Academic Profile
                    </Typography>

                    {data.academic_identity.map((ai) => {
                      return (
                        <>
                          <Typography sx={{ fontSize: 17 }} variant="h3" gutterBottom>
                            <a href={ai.link}>{ai.name}</a> {ai.id}
                          </Typography>
                          <Divider sx={{ my: 2 }} />
                        </>
                      );
                    })}
                    <Typography sx={{ fontSize: 17 }} variant="h3" gutterBottom>
                      {data.citations && `Citations: ${data.citations}`}{' '}
                    </Typography>
                    <Typography sx={{ fontSize: 17 }} variant="h3" gutterBottom>
                      {data.h_index && `H-Index: ${data.h_index}`}
                    </Typography>
                  </CardContent>
                </Card>
              )}
            </Grid>
          </>
        )}
      </Grid>
    </>
  );
};

export default ProfileScreen;
