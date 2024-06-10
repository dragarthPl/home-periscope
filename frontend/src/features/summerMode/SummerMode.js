import {useSelector} from "react-redux";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import WbSunnyIcon from '@mui/icons-material/WbSunny';
import AcUnitIcon from '@mui/icons-material/AcUnit';
import {yellow} from "@mui/material/colors";
import {blue} from "@mui/material/colors";
import ChangeCircleIcon from "@mui/icons-material/ChangeCircle";
import * as React from 'react';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Button from '@mui/material/Button';


const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};


const SummerMode = () => {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const summerMode = useSelector((state) => state.rootReducers.summerMode.summerMode)
    const loadingStatus = useSelector((state) => summerMode === undefined ? 'loading' : 'idle')

    if (loadingStatus === 'loading') {
        return (
          <div className="summer-size">
            <div className="loader" />
          </div>
        )
    }

    return (
      <CardContent>
        <Typography sx={{ fontSize: 14, alignContent: 'center', display: 'flex' }} color="text.secondary" gutterBottom>
            <strong>Tryb: </strong>&nbsp;
            {summerMode ? <WbSunnyIcon sx={{color: yellow[600]}} /> : <AcUnitIcon sx={{color: blue[900]}} />}
            <ChangeCircleIcon sx={{color: blue[600]}} onClick={handleOpen} />
        </Typography>
        <Modal
          open={open}
          onClose={handleClose}
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
        >
          <Box sx={style}>
            <Typography id="modal-modal-title" variant="h6" component="h2">
              Czy na pewno chcesz zmienić tryb pracy pieca ?
            </Typography>
            <Button onClick={handleClose}>Nie</Button>
            <Button onClick={handleClose}>Tak</Button>
          </Box>
        </Modal>
      </CardContent>
    )
}

export default SummerMode;