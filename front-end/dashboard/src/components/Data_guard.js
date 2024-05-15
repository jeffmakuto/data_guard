import React from 'react'
import DisplayTrack from './DisplayData'
import Controls from './Controls'
import ProgressBar from './ProgressBar'
// import { tracks } from '../data'
import Header from './Header'
import Data from './Data'
import 'animate.css';
import './Data.css'
import { useTrack } from '../context/TrackContext'

const MusicPlayer = () => {
    const { trackIndex, handlePlayListItemClick, showPlayList } = useTrack()

    return (
        <div className='Data_guard'>
            <Header onClickPlayList={showPlayList} />
            <div className='Data_guard-body'>
                <div className='player'>
                    <DisplayData />
                    <ProgressBar />
                    <Controls />
                </div>
                <div className='animate__animated animate__slideInLeft'>
                    <PlayList trackIndex={trackIndex} onClick={handlePlayListItemClick} />
                </div>
            </div>
        </div>
    )
}

export default Data_guard