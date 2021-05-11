import {Radio} from './Radio';

export interface PlayerInfo {
  volume: number;
  radio: Radio | any;
  status: string;
  image: string;
}
