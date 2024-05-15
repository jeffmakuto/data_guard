import React, { useState } from 'react'
import Header from './Header'
import Data_guard from './Data_guard'
import './Data.css'
import Data from './Data'

const Player = () => {
    const [view, setView] = useState('Data')

    return (
        <div className='player'>
            <Header onClickPlayList={() => setView('playlist')} />
            {view === 'Data' ? <MData_guard /> : view === 'Data' ? <Data /> : null}
        </div>
    )
}

export default Data