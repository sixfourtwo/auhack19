import * as React from 'react';
import 'office-ui-fabric-react/dist/css/fabric.min.css';
import { Spinner } from 'office-ui-fabric-react';


/**
 * Heavily based on
 * https://medium.com/@650egor/simple-drag-and-drop-file-upload-in-react-2cb409d88929
 */

export interface DragUploadProps {}

export interface DragUploadState {
    dragging: Boolean,
    waiting: Boolean
}

export default class DragUpload extends React.Component<DragUploadProps, DragUploadState> {
    
    // VARIABLES
    dropRef: any = React.createRef();
    dragCounter: number;

    // STATE
    state = {
        dragging: false,
        waiting: false
    }

    // LIFECYCLE
    componentDidMount() {
        this.dragCounter = 0;
        let div = this.dropRef.current;
        div.addEventListener('dragenter', this.handleDragIn);
        div.addEventListener('dragleave', this.handleDragOut);
        div.addEventListener('dragover', this.handleDrag);
        //div.addEventListener('drop', this.handleDrop);
    }

    componentWillUnmount() {
    let div = this.dropRef.current;
    div.removeEventListener('dragenter', this.handleDragIn);
    div.removeEventListener('dragleave', this.handleDragOut);
    div.removeEventListener('dragover', this.handleDrag);
    //div.removeEventListener('drop', this.handleDrop);
    }

    // DRAG EVENT HANDLERS
    handleDrag = (e) => {
        // Just need to override default behavior
        e.preventDefault();
        e.stopPropagation();
    };
    
    handleDragIn = (e) => {
        e.preventDefault();
        e.stopPropagation();
        
        this.dragCounter++;
        this.setState({dragging: true});
        if (e.dataTransfer.items && e.dataTransfer.items.length > 0) {
            this.setState({dragging: true});
          }
    };

    handleDragOut = (e) => {
        e.preventDefault();
        e.stopPropagation();

        this.dragCounter--;
        if(this.dragCounter > 0){
            return;
        }
        this.setState({dragging:false});
    };


    onFileDrop = (e) => {
      e.stopPropagation();
      e.preventDefault();

      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
        //this.props.handleDrop(e.dataTransfer.files)
        e.dataTransfer.clearData();
        this.dragCounter = 0;
        this.setState({dragging:false})
        this.setState({waiting: true});
      }
    }


    // RENDER
    render() {
        return (
          <div
            style={{display: 'block', position: 'absolute', top: '0', bottom: '0', right: '0', left: '0', backgroundColor: 'red'}}
            onDrop={this.onFileDrop} ref={this.dropRef}>
            {this.state.dragging &&
              <div 
                style={{
                  border: 'dashed grey 4px',
                  backgroundColor: 'rgba(255,255,255,.8)',
                  position: 'absolute',
                  top: 0,
                  bottom: 0,
                  left: 0, 
                  right: 0,
                  zIndex: 9999
                }}
              >
                <div 
                  style={{
                    position: 'absolute',
                    top: '50%',
                    right: 0,
                    left: 0,
                    textAlign: 'center',
                    color: 'grey',
                    fontSize: 36
                  }}
                >
                  <div>drop here :)</div>
                </div>
              </div>
            }
            <div style={{ 
              height: '20%',
              width: '80%', 
              borderRadius: '5px',
              margin: 'auto',
              textAlign: 'center', 
              backgroundColor: 'grey'
            }}>Drag pictures here</div>
            {this.state.waiting && Spinner}
          </div>
        )
      }

}