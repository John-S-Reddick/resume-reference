import axios from "axios";
import { createRoot } from 'react-dom/client'
import { createElement } from 'react';
import React, { useState, useEffect } from 'react';
import {
   Button, Card, Col,
   Container, Dropdown, Image,
   Navbar, NavLink, Row, Stack
   } from 'react-bootstrap';

const genres = ["---", "Pop","Rock","Hip hop","Country",
  "R&B/Soul","Electronic",
  "Jazz","Classical",
  "Blues","Gospel",
  "Reggae","Latin",
  "Folk","Alternative",
  "Punk","Metal",
  "Indie","Funk",
  "World","Americana"];

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

async function credify(){
        let client_id = 'ec11cb8823c14142845468f945f6abc2';
        let client_secret = 'd2609b60cae545c584cac52e52502e65';
        let myHeaders = new Headers();
        let encodedCreds = btoa(client_id + ':' + client_secret);
        myHeaders.append("Authorization", `Basic ` + encodedCreds);
        myHeaders.append("Content-Type", "application/x-www-form-urlencoded");

        var urlencoded = new URLSearchParams();
        urlencoded.append("grant_type", "client_credentials");

        const requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: urlencoded,
        redirect: 'follow'
        }
        let res = await fetch("https://accounts.spotify.com/api/token", requestOptions);
        res = await res.json();
        var output = await res.access_token;
        return output; 
    }

async function singleQuery(target, accessToken){
    let myHeaders = new Headers();
    let RAT = await accessToken;
    myHeaders.append("Authorization", "Bearer " + RAT);
    myHeaders.append("Content-Type", "application/json");
    const requestOptions = {
        method: 'GET',
        headers: myHeaders,
    }
    var k = 0;
    let res = await fetch("https://api.spotify.com/v1/search?q=genre:" +
                          target + "&type=track&limit=50&offset=1",requestOptions)
            .then(response1 => response1.json())
            .then(result => {
                k = getRandomInt(result.tracks.total);
            });
    let refine = await fetch("https://api.spotify.com/v1/search?q=genre:" +
          target + "&type=track&limit=1&offset=" + k,requestOptions)
    .then(response2 => response2.json())
    .then(refined => {
        const songObject = {
        songLink: "http://open.spotify.com/track/" + refined.tracks.items[0].id,
        trackAlbumName: refined.tracks.items[0].album.name,
        trackAlbumArt: refined.tracks.items[0].album.images[0].url,
        trackArtist: refined.tracks.items[0].artists[0].name,
        trackName: refined.tracks.items[0].name            
        };
        return songObject;
    });
    return refine
}

async function gimme(tar1, tar2, tar3){
    const creds = credify();
    const track1 = await singleQuery(tar1, creds);
    console.log(track1);
    const track2 = await singleQuery(tar2, creds);
    console.log(track2);
    const track3 = await singleQuery(tar3, creds);
    console.log(track3);
    // THESE OBJECTS WILL HAVE VALUES BY THIS POINT.
    // SEND THE INFORMATION TO THE UI
    // These horrible assignments are here because decomposition didn't work.
    const SL1 = await track1.songLink;
    const TAN1 = await track1.trackAlbumName;
    const TAR1 = await track1.trackAlbumArt;
    const ART1 = await track1.trackArtist;
    const NAM1 = await track1.trackName;

    
    const SL2 = await track2.songLink;
    const TAN2 = await track2.trackAlbumName;
    const TAR2 = await track2.trackAlbumArt;
    const ART2 = await track2.trackArtist;
    const NAM2 = await track2.trackName;
    
    const SL3 = await track3.songLink;
    const TAN3 = await track3.trackAlbumName;
    const TAR3 = await track3.trackAlbumArt;
    const ART3 = await track3.trackArtist;
    const NAM3 = await track3.trackName;
    
    const bucket = createRoot(document.getElementById('targetStack'));
    bucket.render(<> 
      <Cardo name={NAM1} album={TAN1} artist={ART1} cover={TAR1} link={SL1}/>
      <Cardo name={NAM2} album={TAN2} artist={ART2} cover={TAR2} link={SL2}/> 
      <Cardo name={NAM3} album={TAN3} artist={ART3} cover={TAR3} link={SL3}/> 
                  </>);

}

function Navibar(){
    return(
        <Navbar bg="dark" variant="dark" fluid expand="lg">
        <Container>
          <Navbar.Brand href="#home">Underground Sound</Navbar.Brand>          
          <Navbar.Text text = "dark">
            Group 8
          </Navbar.Text>
        </Container>
      </Navbar>
    );
}


function Cardo({name, album, artist, cover, link}) {
    return(
      <Container>
        <Card  bg="dark" key="dark" text="light">
        <Col align="center">
          <Image variant="top" 
            src={cover} 
            width={400}
            height={400}
            object-fit = "cover"/>
            </Col>
          
          <Card.Body>
            <Card.Title>{name}</Card.Title>
            <Card.Text> <b2>
            {artist} <br /> {album}
            </b2> </Card.Text>
          </Card.Body>
          <Card.Footer>
            <small className="text-muted"><a href={link}>Check out this song here!</a></small>
          </Card.Footer>
        </Card>
      </Container>
    );
}


function MyDropdown({onSelect, title}) {
  const [selectedItem, setSelectedItem] = useState(title);

  const handleSelect = (eventKey) => {
    setSelectedItem(eventKey);
    onSelect(eventKey);
  };

  return (
    <Col align="center">
      <Row>
        <Dropdown onSelect={handleSelect} id="dropdown-basic" as={Button} size="lg" variant="dark">
          <Dropdown.Toggle as={NavLink} variant="dark">
            {selectedItem}
          </Dropdown.Toggle>
          <Dropdown.Menu variant="dark">
            {genres.map((g, index) => (
              <Dropdown.Item key={index} eventKey={g}>
                {g}
              </Dropdown.Item>
            ))}
          </Dropdown.Menu>
        </Dropdown>
      </Row>
    </Col>
  );
}

function GenreSubmit(){

  const [selections, setSelections] = useState({});

  const handleDropdownSelect = (id, option) => {
    setSelections((prevState) => ({ ...prevState, [id]: option }));
  };

  const handleSubmit = () => {
    var selected = [];
    var safe = false;
    var target1 = '';
    var target2 = '';
    var target3 = '';
      
        for (var key in selections){
        if (selections.hasOwnProperty(key)) {
            if (selections[key] != '---') {
                selected.push(selections[key]);
                }
        }
    } 
    switch(selected.length) {
        case 3:
            target1 = selected[0];
            target2 = selected[1];
            target3 = selected[2];
            safe = true;
            break;
        case 2:
            target1 = selected[0];
            target2 = selected[1];
            target3 = selected[0];
            safe = true;
            break;
        case 1:
            target1 = selected[0];
            target2 = selected[0];
            target3 = selected[0];
            safe = true;
            break;
        default:
            console.log("Nothing selected!");
            safe = false;      
    }
    if (safe) {
        gimme(target1, target2, target3); 
    }
      
  };

  return(        
  
      <Stack gap={5}>
        <p/>
        <p/>     
      <Stack direction="horizontal" gap={5}>
        <MyDropdown
            onSelect={(option) => handleDropdownSelect('dropdown', option)}
            title = 'Genre 1'
          />
        <MyDropdown
            onSelect={(option) => handleDropdownSelect('dropdown2', option)}
            title = 'Genre 2'
          />
        <MyDropdown
            onSelect={(option) => handleDropdownSelect('dropdown3', option)}
            title = 'Genre 3'
          />
      </Stack>
        <Col md={{ span: 4, offset: 4 }}>
          <Row>
            <Button size="lg" variant="success" onClick={handleSubmit}>
              Submit
            </Button>
          </Row>
        </Col>
        <p/>
    </Stack>


  );

}


function getSelectedGenres() {
  const dropdowns = document.querySelectorAll('#dropdown-basic');
  const selectedGenres = [];
  dropdowns.forEach((dropdown) => {
    selectedGenres.push(dropdown.innerText);
  });
  return selectedGenres;
}

function TopHalf(){
    let underGroundLogoWidth = 1760
    let underGroundLogoHeight = 274
    let scalingUnderGround = 1/2
    let cx = 1600
    let cy = 1280
    let cs = .26


    return(
      <div>
        <Row>
          <p></p>
        <Col align="left" sm="5">
            <Image 
            width={scalingUnderGround * underGroundLogoWidth}
            height={scalingUnderGround * underGroundLogoHeight}
            src="https://cdn.discordapp.com/attachments/1070029271810183258/1100967625820995615/Underground_Sound2x.png"/>
            <Col md={{ span: 15, offset: 1 }}>
            <p></p>
              <h4 >
                Welcome to Underground Sound! 
              </h4>
              <h5>
                To get started, just select at least one genre
                from the menus below and hit Search
              </h5>
            </Col>

        </Col>

        <Col sm="3"></Col>

        <Col sm="3">
          <Image width={cs * cx} height={cs * cy} src="https://media.discordapp.net/attachments/1067501991988822030/1100937420138098748/UndergroundSoundLogo.png?width=839&height=671"/>
        </Col>
      </Row>
      <Container>
        <GenreSubmit/>
      </Container>
          </div>
    );


  }

  function Layout() {
    return (
      <div>
          <Navibar/>
          <Row>
            <Col sm = "1"></Col>
            <Col sm = "10">
              <Stack gap={3}>
                  <TopHalf/>
                  <Stack direction="horizontal" gap={3} id="targetStack">
                  </Stack>
              </Stack>
            </Col>
            <Col sm = "1"></Col>
          </Row>
      </div>
    );
  }
  
  export default Layout;