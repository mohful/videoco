import './App.css';
import { Amplify } from 'aws-amplify';
import { Authenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import { Box, Grid, Typography } from '@mui/material'
import { View, Image } from '@aws-amplify/ui-react';
import { useTheme } from '@aws-amplify/ui-react';
import awsExports from './aws-exports';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { NavBar } from './components/NavBar';

Amplify.configure(awsExports);

const appStyles = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  height: '100vh', // Adjust this as needed
};


const components = {
  Header() {
    const { tokens } = useTheme();
    return (
      <Box sx={{display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <View padding={tokens.space.large}>
          <Image
            alt="Amplify logo"
            src="https://docs.amplify.aws/assets/logo-dark.svg"
          />
        </View>
        {/* <img src={logo} alt='logo' /> */}
      </Box>
    )
  },

  SignUp: {},

  Footer() {
    return (
      <Grid item container xs={12} sx={{display:'flex', justifyContent:'center',alignItems:'center', height:'100%'}}>
        <View>
          <Typography align='center' variant='subtitle1' color='text.secondary'>Copyright VideoCo &copy; 2022 | All Rights Reserved</Typography>
        </View>
      </Grid>
    )
  }
}


export default function App() {
  return (
    <div style={appStyles}>
      <Authenticator components={components}>
        {({ signOut, user }) => (
          <BrowserRouter>
          <NavBar>
            {/* <Routes>

            </Routes> */}
          </NavBar>
          </BrowserRouter>
        )}
      </Authenticator>
    </div>
  );
}