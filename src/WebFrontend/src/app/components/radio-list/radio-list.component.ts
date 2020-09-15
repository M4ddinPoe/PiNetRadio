import { Component, OnInit } from '@angular/core';
import {RadioRepository} from '../../Repositories/RadioRepository';
import {Radio} from '../../../models/Radio';

@Component({
  selector: 'radio-list',
  templateUrl: './radio-list.component.html',
  styleUrls: ['./radio-list.component.scss']
})
export class RadioListComponent implements OnInit {

  private radioRepository: RadioRepository;
  private isPlaying = false;

  public radios: Array<Radio>;

  constructor(radioRepository: RadioRepository) {
    this.radioRepository = radioRepository;
  }

  ngOnInit(): void {
    this.radioRepository.getRadios().then((radios: Array<Radio>): void => {
      this.radios = radios;
    });
  }

  playOrStop(num: number): void {
    if (this.isPlaying) {
      this.radioRepository.playRadio(num);
    }
    else {
      this.radioRepository.stopRadio(num);
    }

    this.isPlaying = !this.isPlaying;
  }

}
