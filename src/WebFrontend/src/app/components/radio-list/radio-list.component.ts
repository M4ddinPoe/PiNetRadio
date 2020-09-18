import { Component, OnInit } from '@angular/core';
import {RadioRepository} from '../../Repositories/RadioRepository';
import {Radio} from '../../../models/Radio';
import {LocalStorageRepository} from "../../repositories/LocalStorageRepository";

@Component({
  selector: 'radio-list',
  templateUrl: './radio-list.component.html',
  styleUrls: ['./radio-list.component.scss']
})
export class RadioListComponent implements OnInit {

  public radios: Array<Radio>;
  public currentRadio: Radio;
  public volume = 50;
  public isPlaying = false;

  private radioRepository: RadioRepository;
  private localStorage: LocalStorageRepository;

  constructor(radioRepository: RadioRepository,
    localStorage: LocalStorageRepository) {
    this.radioRepository = radioRepository;
    this.localStorage = localStorage;
  }

  ngOnInit(): void {
    this.radioRepository.getRadios().then((radios: Array<Radio>): void => {
      this.radios = radios;
    });

    this.currentRadio = this.localStorage.getLastRadio();
    this.volume = this.localStorage.getLastVolume();
  }

  public async playRadio(radio: Radio): Promise<void> {
    await this.radioRepository.playRadio(radio.id);
    this.currentRadio = radio;
    this.isPlaying = true;

    this.localStorage.setLastRadio(this.currentRadio);
  }

  public async playOrStop(): Promise<void> {
    if (this.isPlaying) {
      await this.radioRepository.stopRadio();
    }
    else {
      await this.radioRepository.playRadio(0);
    }

    this.isPlaying = !this.isPlaying;
  }

  public async volumeUp(): Promise<void> {
    this.volume = this.volume + 2;
    await this.updateVolume();
  }

  public async volumeDown(): Promise<void> {
    this.volume = this.volume - 2;
    await this.updateVolume();
  }

  public async updateVolume(): Promise<void> {
    await this.radioRepository.setVolume(this.volume);
    this.localStorage.setLastVolume(this.volume);
  }

}
