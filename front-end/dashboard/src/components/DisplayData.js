import React from 'react'
import './DisplayData.css'
import { useData } from '../context/DataContext'

const Data = () => {
    const { data, dataRef, setDuration, progressBarRef, handleNext } = useData()

    function onLoadedMetadata() {
        const duration = audioRef.current.duration
        setDuration(duration)
        progressBarRef.current.max = duration
    }

    return (
        <div className='display-data-container'>
            <img className='data-image-preview-rounded' src={data.coverUrl} alt='data' />
            <div className='data-info'>
                <h4 className='data'>{data.displayName}</h4>
                <p className='data'>{track.artist}</p>
            </div>
            <audio src={track.audioSrc} ref={audioRef} onLoadedMetadata={onLoadedMetadata} onEnded={handleNext} />
        </div>
    )
}

export default DisplayTrack