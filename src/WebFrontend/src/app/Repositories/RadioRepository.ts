import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Radio} from '../../models/Radio';
import {Injectable} from '@angular/core';
import {PlayerInfo} from '../../models/PlayerInfo';
import {InfoResponse} from './models/InfoResponse';

@Injectable({
  providedIn: 'root',
})
export class RadioRepository {
  private httpClient: HttpClient;

  private webAPIUrl = 'http://localhost:5000/api/';

  constructor(httpClient: HttpClient) {
    this.httpClient = httpClient;
  }

  public async info(): Promise<PlayerInfo> {
    try {
      const url = this.webAPIUrl + 'info';

      const headers: HttpHeaders = new HttpHeaders()
        .set('accept', 'application/json');

      const response: InfoResponse =
        await this.httpClient.get<InfoResponse>(url, {headers: headers})
          .toPromise();

      return response.info;
    } catch (error) {
      console.log('Error: ' , error);
    }
  }

  public async getRadios(): Promise<Array<Radio>> {
    try {
      const url = this.webAPIUrl + 'radios';

      const headers: HttpHeaders = new HttpHeaders()
        .set('accept', 'application/json');

      const response: Array<Radio> =
        await this.httpClient.get<Array<Radio>>(url, {headers: headers})
          .toPromise();

      return response;
    } catch (error) {
      console.log('Error: ' , error);
    }
  }

  public async playRadio(num: number): Promise<any> {
    try {
      const url = this.webAPIUrl + 'radios/' + num + '/play';

      const headers: HttpHeaders = new HttpHeaders()
        .set('accept', 'application/json');

      const response: any =
      await this.httpClient.get(url, {headers: headers})
          .toPromise();

      return response;
    } catch (error) {
      console.log('Error: ' , error);
    }
  }

  public async stopRadio(): Promise<any> {
    try {
      const url = this.webAPIUrl + 'radios/stop';

      const headers: HttpHeaders = new HttpHeaders()
        .set('accept', 'application/json');

      const response: any =
        await this.httpClient.get(url, {headers: headers})
          .toPromise();

      return response;
    } catch (error) {
      console.log('Error: ' , error);
    }
  }

  public async setVolume(num: number): Promise<any> {
    try {
      const url = this.webAPIUrl + 'radios/volume/' + num;

      const headers: HttpHeaders = new HttpHeaders()
        .set('accept', 'application/json');

      const response: any =
        await this.httpClient.get(url, {headers: headers})
          .toPromise();

      return response;
    } catch (error) {
      console.log('Error: ' , error);
    }
  }

  public async shutdown(): Promise<any> {
    try {
      const url = this.webAPIUrl + 'system/shutdown';

      const headers: HttpHeaders = new HttpHeaders()
        .set('accept', 'application/json');

      const response: any =
        await this.httpClient.get(url, {headers: headers})
          .toPromise();

      return response;
    } catch (error) {
      console.log('Error: ' , error);
    }
  }
}
