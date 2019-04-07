import * as React from 'react';
//import { Button, ButtonType } from 'office-ui-fabric-react';
//import Header from './Header';
//import HeroList, { HeroListItem } from './HeroList';
import DragUpload from './dragupload/DragUpload';
import Progress from './Progress';



export interface AppProps {
    title: string;
    isOfficeInitialized: boolean;
}

export interface AppState {
    // listItems: HeroListItem[];
}

export default class App extends React.Component<AppProps, AppState> {
    constructor(props, context) {
        super(props, context);
        this.state = {
            listItems: []
        };
    }

    componentDidMount() {
        this.setState({
            listItems: [
                {
                    icon: 'Ribbon',
                    primaryText: 'Achieve more with Office integration'
                },
                {
                    icon: 'Unlock',
                    primaryText: 'Unlock features and functionality'
                },
                {
                    icon: 'Design',
                    primaryText: 'Create and visualize like a pro'
                }
            ]
        });
    }

    click = async () => {
        /**
         * Insert your Outlook code here
         */
    }

    render() {
        const {
            title,
            isOfficeInitialized,
        } = this.props;

        if (!isOfficeInitialized) {
            return (
                <Progress
                    title={title}
                    logo='assets/logo-filled.png'
                    message='Please sideload your addin to see app body.'
                />
            );
        }

        return (
            <div className='ms-welcome'>
                <DragUpload/>
            </div>
        );
    }
}
