import React from "react";
import { Card,Col} from "react-bootstrap";
import { Grid } from 'semantic-ui-react'
import "bootstrap/dist/css/bootstrap.min.css";
import "./info.css";
import {API_BASE_URL} from '../../constants'

function InfoCardList(props) {
    var dat = props.updated
    var st = String(dat)
    var shot_d = st.substring(0,10)
    if (props.title) {
        console.log(props.title)
        console.log(props.content)
        console.log(props)
        console.log(props.id,'id')
    }
  return (
      <div class="outer">
    <Grid columns='equal'>
      <Grid.Column>
    <Col md="auto">
      <Card
        className="bg-dark text-white"
      >
        <Card.Img src={API_BASE_URL+props.imgg} alt="Card image" class="image-container contrast" />
        <Card.ImgOverlay>
            <div class="inner">
          <h1>
              <a href={`/info/detail/${props.id}`}>{props.title}</a>
          </h1>
          <Card.Title >발행일 : {shot_d}</Card.Title>
          </div>
        </Card.ImgOverlay>
      </Card>
    </Col>
    </Grid.Column>
    </Grid>
          </div>
  );
}

export default InfoCardList;
